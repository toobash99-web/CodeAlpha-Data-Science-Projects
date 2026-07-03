# 1. Import the tools we just installed
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# 2. Setup: We pretend to be a real browser so websites don't block us.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# 3. We will store all our scraped data in this list
all_posts = []

# 4. We will scrape pages 1 to 5 (each page has 30 posts. 5 pages = 150 posts)
for page_number in range(1, 6):
    print(f"Scraping Page {page_number}...")
    
    # Build the URL (Hacker News uses ?p=2 for page 2)
    url = f"https://news.ycombinator.com/show?p={page_number}"
    
    # Step A: Ask the website for the HTML
    response = requests.get(url, headers=HEADERS)
    
    # Step B: Feed the HTML text to BeautifulSoup for parsing
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Step C: Find all rows that contain a post (they are in <tr> with class 'athing')
    post_rows = soup.find_all("tr", class_="athing")
    
    # Step D: Loop through each post row to extract data
    for row in post_rows:
        # --- TITLE & URL ---
        # Find the first <a> tag inside the 'titleline' span
        titleline = row.find("span", class_="titleline")
        if titleline:
            link = titleline.find("a")
            title = link.text if link else "No Title"
            url_link = link.get("href") if link else "No URL"
            # Check if it's an internal HN story or external link
            if url_link.startswith("item"):
                url_link = "https://news.ycombinator.com/" + url_link
        else:
            title = "No Title"
            url_link = "No URL"
        
        # --- RANK (What position is it on the page?) ---
        rank_span = row.find("span", class_="rank")
        rank = rank_span.text.replace(".", "") if rank_span else "0"
        
                # --- SCORE (Upvotes) & USER (FIXED VERSION) ---
        # The subtext is always in the very next table row (<tr>) after the title row.
        next_row = row.find_next_sibling("tr")
        
        # Default values in case we find nothing
        score = "0"
        user = "Anonymous"
        comments = "0"
        
        if next_row:
            # 1. Grab the Upvotes (look for the 'score' class)
            score_span = next_row.find("span", class_="score")
            if score_span:
                score = score_span.text.split()[0]  # Gets just the number
            
            # 2. Grab the Username (look for the 'hnuser' class)
            user_span = next_row.find("a", class_="hnuser")
            if user_span:
                user = user_span.text
            
            # 3. Grab Comments (look for the last link containing 'comment')
            comment_links = next_row.find_all("a")
            for link in comment_links:
                if "comment" in link.text.lower():
                    comments = link.text.split()[0]
                    break
        
        # --- Save everything into a dictionary ---
        post_data = {
            "Rank": int(rank),
            "Title": title,
            "Domain": url_link.split("/")[2] if "http" in url_link else "Internal",
            "Upvotes": int(score),
            "User": user,
            "Comments": int(comments),
            "URL": url_link
        }
        
        # Add to our master list
        all_posts.append(post_data)
    
    # BE POLITE! Wait 2 seconds before hitting the next page, so we don't crash their server.
    time.sleep(2)

# 5. Convert our list into a beautiful table (DataFrame) using Pandas
df = pd.DataFrame(all_posts)

# 6. Save it to an Excel file for your portfolio
df.to_excel("showhn_launch_data.xlsx", index=False)

print(f"SUCCESS! Scraped {len(all_posts)} posts. Check the Excel file!")