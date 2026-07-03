import pandas as pd

# Load your freshly scraped data
df = pd.read_excel("showhn_launch_data.xlsx")

# 1. ANALYSIS: Which domains do founders love?
domain_counts = df['Domain'].value_counts().head(10)
print("🏆 Top 10 Domains used by founders:")
print(domain_counts)
print("\n" + "="*30)

# 2. ANALYSIS: Does title length matter? (Short vs Long)
df['Title_Length'] = df['Title'].str.len()
avg_upvotes_short = df[df['Title_Length'] < 50]['Upvotes'].mean()
avg_upvotes_long = df[df['Title_Length'] >= 50]['Upvotes'].mean()

print(f"📊 Average Upvotes for SHORT titles (<50 chars): {avg_upvotes_short:.1f}")
print(f"📊 Average Upvotes for LONG titles (>=50 chars): {avg_upvotes_long:.1f}")

# 3. EXPORT: Create a tailored summary dataset for your portfolio
summary_df = df.groupby('Domain').agg(
    Total_Upvotes=('Upvotes', 'sum'),
    Average_Upvotes=('Upvotes', 'mean'),
    Count=('Title', 'count')
).sort_values('Total_Upvotes', ascending=False).head(20)

# Save this custom analysis to a new Excel file
summary_df.to_excel("startup_launch_insights.xlsx")
print("\n✅ ANALYSIS COMPLETE! Check 'startup_launch_insights.xlsx'")