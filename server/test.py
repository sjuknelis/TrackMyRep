from functools import cmp_to_key
import spacy
import pytextrank
text = """
SKIP TO CONTENTSKIP TO SITE INDEX
Student Loan
Debt Relief
Your Questions, Answered
Biden Announces His Decision
Possible Effects on Inflation
Biden to Cancel $10,000 in Student Loan Debt; Low-Income Students Are Eligible for More
The debt forgiveness comes after months of deliberations in the White House over fairness and fears that the plan could exacerbate inflation before the midterms.

Give this article

1.9K
Protesters outside the Education Department in Washington in April. The question of how far the United States should go in providing debt forgiveness has emerged as one of the most contentious issues for President Biden.
Protesters outside the Education Department in Washington in April. The question of how far the United States should go in providing debt forgiveness has emerged as one of the most contentious issues for President Biden.Credit...Kenny Holston for The New York Times
Zolan Kanno-YoungsStacy CowleyJim Tankersley
By Zolan Kanno-Youngs, Stacy Cowley and Jim Tankersley
Aug. 24, 2022
Updated 2:01 p.m. ET
WASHINGTON — President Biden announced on Wednesday that he would cancel $10,000 in student loan debt for those earning less than $125,000 per year, with an additional $10,000 for those who had received Pell grants for low-income students, providing economic relief for tens of millions of Americans.

The debt forgiveness, although less than the amount that some Democrats had been pushing for, comes after months of deliberations in the White House over fairness and fears that it could exacerbate inflation before the midterm elections. The plan will almost certainly face legal challenges, making the timing of any relief uncertain.

In a Twitter post outlining some details of his plan, Mr. Biden said a pandemic-era pause on student loan payments, which has been in effect since March 2020, would expire at the end of the year.

“In keeping with my campaign promise, my Administration is announcing a plan to give working and middle class families breathing room as they prepare to resume federal student loan payments in January 2023,” the president said.

Across the United States, 45 million people owe $1.6 trillion for federal loans taken out for college — more than they owe on car loans, credit cards or any consumer debt other than mortgages. Current students are also eligible for the debt relief; if they are dependents they will be assessed based on their parents’ income.

To our readers:
Stories like this are possible because of our deep commitment to original reporting, produced by a global staff of over 1,700 journalists who have all dedicated themselves to helping you understand the world. That work is only possible because of the support of our subscribers. I hope you’ll consider becoming one today.

— Marc Lacey, Managing Editor

Mr. Biden has been agonizing over how to address student loans for months, and the issue has become an uncomfortable political problem for him. Mr. Biden has been under pressure from progressive Democrats who say debt forgiveness is necessary to address racial disparities in the economy. But critics say widespread debt forgiveness is unfair to those who tightened their belts to pay for college. Republicans and some Democrats contend that it will add to inflation by giving consumers more money to spend.

Dig deeper into the moment.
Special offer: Subscribe for $1 a week.
The White House sought to address those economic concerns by carefully targeting the relief.

Students who received Pell grants will be eligible for $20,000 in debt forgiveness. Around 60 percent of borrowers have received Pell grants, and the majority come from families making less than $30,000 a year. The Education Department estimates that 27 million borrowers will qualify for up to $20,000 in relief.

“I was standing in my dorm room when I heard this and I just let out a scream,” said Marlene Ramirez, who relied on Pell grants and other aid to pay for her undergraduate studies.

Millions of other borrowers will be eligible for $10,000 in debt relief, as long as they earn less than $125,000 a year or are in households earning less than $250,000. The administration contends that 90 percent of the relief will go to households earning $75,000 a year or less.

Ms. Ramirez, whose parents immigrated from Mexico, was the first in her family to go to college. She used Pell grants to cover two years of study at a community college, than transferred to the University of California, Los Angeles, and graduated in 2020 with a bachelor’s degree in anthropology. Scholarships and aid covered her tuition, but she has $25,000 in federal loans that she used to cover her housing and living expenses.

What to Know About Student Loan Debt Relief
Card 1 of 5
Many will benefit. President Biden’s executive order means the federal student loan balances of millions of people could fall by as much as $20,000. Here are answers to some common questions about how it will work:

Who qualifies for loan cancellation? Individuals who are single and earn $125,000 or less will qualify for the $10,000 in debt cancellation. If you’re married and file your taxes jointly or are a head of household, you qualify if your income is $250,000 or below. If you received a Pell Grant and meet these income requirements, you could qualify for an extra $10,000 in debt cancellation.

What’s the first thing I need to do if I qualify? Check with your loan servicer to make sure that your postal address, your email address and your mobile phone number are listed accurately, so you can receive guidance. Follow those instructions. If you don’t know who your servicer is, consult the Department of Education’s “Who is my loan servicer?” web page for instructions.

How do I prove that I qualify? If you’re already enrolled in some kind of income-driven repayment plan and have submitted your most recent tax return to certify that income, you should not need to do anything else. Still, keep an eye out for guidance from your servicer. For everyone else, the Education Department is expected to set up an application process by the end of the year.

When will payments for the outstanding balance restart? President Biden extended a Trump-era pause on payments, which are now not due until at least January. You should receive a billing notice at least three weeks before your first payment is due, but you can contact your loan servicer before then for specifics on what you owe and when payment is due.

“This will almost wipe that out,” said Ms. Ramirez, 25, who is finishing a master’s degree at the London School of Economics. “I’m shaking right now — this is life-changing.”

Mr. Biden also proposed various changes to the repayment system — which would need to be implemented through rule-making by the Education Department — that would slash many borrowers’ monthly bills. He is seeking to let those with undergraduate loans cap their payments at 5 percent of their discretionary monthly income, down from the 10 percent ceiling currently in place on most income-based payment plans.

He is also seeking to have the government cover the monthly interest for those making payments — even if their payment is zero, because their income is low — so that borrowers’ balances won’t balloon. Under the current system, interest still accrues, and many borrowers find themselves falling deeper into debt even as they make their monthly payments.

What we consider before using anonymous sources. How do the sources know the information? What’s their motivation for telling us? Have they proved reliable in the past? Can we corroborate the information? Even with these questions satisfied, The Times uses anonymous sources as a last resort. The reporter and at least one editor know the identity of the source.

Learn more about our process.
On its face, the move could cost taxpayers about $300 billion or more in money they effectively lent out that will never be repaid. But the true cost is harder to calculate, and likely to be smaller, because much of that debt was unlikely to ever be repaid. More than eight million people — one in five borrowers with a payment due — had defaulted on their loans before the coronavirus pandemic. Many of those people carried fairly small balances and will now be eligible to have their loans canceled.

Many Democratic lawmakers and progressive groups had argued that addressing economic racial disparities would require forgiving $50,000 of debt, citing reports showing that Black and other nonwhite borrowers end up with higher average loan balances than their white peers.

Representative Tony Cárdenas, a California Democrat who met with the White House to advocate debt cancellation, said even the limited relief could be the galvanizing factor Mr. Biden’s party needs before the midterms in November.

“That’s a lot of young people that are going to be able to have a sigh of relief,” Mr. Cárdenas said. He said the plan would let them “look forward to buying a house soon; they could look forward to starting a family sooner.”

He and other members of the Hispanic Caucus helped ramp up pressure on Mr. Biden this spring, when they said he indicated in a private meeting that he intended to provide some form of debt relief for Americans. Shortly afterward, the president publicly said he was considering the move and would announce details in the coming weeks.

But inside the White House, Mr. Biden’s top aides were debating the political and economic ramifications of the decision. According to people familiar with his thinking, the president was concerned that loan cancellation would be seen as a giveaway that would be an affront to those who had paid their or their relative’s tuition. Some top aides also argued that Mr. Biden lacked the legal authority to move forward with the sweeping loan forgiveness and that he should work with Congress instead of using executive action.

Soaring inflation also complicated the process.

“In the middle of crushing Biden-flation, how could the president justify a student loan giveaway that overlooks Americans hurt most by inflation?” Representative Kevin Brady of Texas, the top Republican on the Ways and Means Committee, said last month.

Mr. Biden’s economic advisers, however, made the case that by resuming loan payments and pairing the loan forgiveness with income caps, the cancellation would have a negligible effect on rising consumer prices. The president’s chief of staff, Ron Klain, also advised him that providing relief could galvanize young voters who are increasingly frustrated with him.

Senate Democrats continued to make direct appeals to the White House in the days leading up the decision. Senator Charles Schumer of New York, the majority leader, as well as Senators Elizabeth Warren of Massachusetts and Raphael Warnock of Georgia, met with Mr. Klain and Brian Deese, one of Mr. Biden’s top economic advisers, to lobby the White House on student loan forgiveness.

Mr. Schumer spoke with Mr. Biden on Tuesday night to ask him to cancel as much debt as possible, according to a Democrat familiar with the conversation.

Legal challenges are expected, although who would have the standing to press their case in court is unclear. A recent Virginia Law Review article argued that the answer might be no one: States, for example, have little say in the operation of a federal loan system.

Mary-Pat Hector, a graduate student at Georgia State University, said Mr. Biden’s move was an important first step to support those disappointed by the administration’s failure to accomplish other policy goals, such as providing two free years of community college.

“They were told: Vote because your life depends on it,” said Ms. Hector, 23, who has $50,000 in loans from Spelman College. “And then we’re here on the ground, months away from midterm elections, and people in these communities are wondering, ‘Well, does my vote really matter?’”

In addition to college debt, Ms. Hector said her mother also borrowed to pay for her education. She criticized the administration’s decision to impose limits on who would receive loan forgiveness based on salary, noting that while some of her peers earned a healthy income, they would also be responsible for supporting younger siblings who might borrow to attend college.

“You’re still in inescapable debt from school, and you’re still taking care of your family and community,” said Ms. Hector, an activist with the organization Rise, which has pushed for loan forgiveness. “My parents are probably in lifetime debt to get me in that position, and I’m going to have to repay them by ensuring my little brother is going to school. That’s the pressure you have.”


Biden to Announce Decision on Student Debt, Affecting Millions of Borrowers
Aug. 23, 2022

7 Million Bad Student Loans With No Way Out, for Anyone
May 25, 2022
Zolan Kanno-Youngs is a White House correspondent covering a range of domestic and international issues in the Biden White House, including homeland security and extremism. He joined The Times in 2019 as the homeland security correspondent. @KannoYoungs

Stacy Cowley is a finance reporter with a focus on consumer issues and data security. She previously reported on a variety of business topics, including technology and economics, at CNN Money, Fortune Small Business, and other magazines and websites. @StacyCowley

Jim Tankersley is a White House correspondent with a focus on economic policy. He has written for more than a decade in Washington about the decline of opportunity for American workers, and is the author of "The Riches of This Land: The Untold, True Story of America's Middle Class." @jimtankersley

READ 1864 COMMENTS
Give this article

1.9K
A Guide to Student Loans
Are you a new graduate or a family starting to think about how to pay for college? These tips can help you navigate student finances.
Before College Starts

This introduction to student loans can help you understand what you might be signing up for.

Consider the “return on investment”: Will that college degree pay itself off?

Think twice before taking a private student loan. They carry fewer protections than federal loans and tend to be more expensive.

Colleges’ financial aid offers are not always easy to decipher. These tips can help you make sense of the jargon.

After Graduation

Could the government’s Public Service Loan Forgiveness Program be the right fit for you? Here is what you should know about it.

Beware of the repayment traps you might incur, and learn how to avoid them.

Are you a recent graduate about to make your first repayment? Make sure you know how much you owe, and to whom.

More in U.S. News
Chris Stirewalt, a former Fox News journalist, appeared in June before the House committee investigating the Capitol riot.
Doug Mills/The New York Times
A Former Fox News Insider Spills the Beans
Aug. 20
Continue reading the main story
Paul Pelosi, the husband of House Speaker Nancy Pelosi, in Washington in March.
Andrew Harnik/Associated Press
Pelosi’s Husband Pleads Guilty to D.U.I. After California Crash
Aug. 23
Much of the presidential archive is transferred digitally, which makes it all the more striking that Donald J. Trump appears to have taken so many paper documents.
Jamie Kelter Davis for The New York Times
Trump Flouted Rules About Presidential Records. That’s Not How It Usually Works.
Aug. 23
Editors' Picks
Amber Escudero-Kontostathis, 28, was the sole survivor of a deadly lightning strike near the White House.
Haiyun Jiang/The New York Times
Survivor of White House Lightning Strike Embraces Third Chance at Life
Aug. 19

Linda Xiao for The New York Times. Food Stylist: Sarah Jampel.
14 Easy 15-Minute Dinners for When There Aren’t Enough Hours in the Day
Aug. 19
Most Popular
Why Are My Son’s New Wife and Baby Living at Her Parents’ House?
A Novelist Chronicles the Panic of War While Living Through It
Brown University Acquires the Papers of Mumia Abu-Jamal
Can an Iconic Italian Wool Survive a Changing Economy?
A Lodge for All Seasons Nestled at the Foot of a Mountain
Could New Zealand Change Its Name?
Teenage Aviator Circles the Globe Solo, Setting a Record
For Chernobyl Survivors, New Ukraine Nuclear Risk Stirs Dread
Latisha Chong, Hair Stylist Who Helped Change Fashion, Dies at 32
Tell us about yourself. Take our survey.

Take our survey.
Site Index
Go to Home Page »
NEWS
OPINION
ARTS
LIVING
LISTINGS & MORE
Site Information Navigation
© 2022 The New York Times Company
NYTCoContact UsAccessibilityWork with usAdvertiseT Brand StudioYour Ad ChoicesPrivacy PolicyTerms of ServiceTerms of SaleSite MapCanadaInternationalHelpSubscriptions"""

def compare_phrases(a,b):
  return -(a.rank * a.count - b.rank * b.count)

# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")
# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")

doc = nlp(text)
phrases = doc._.phrases
phrases.sort(key=cmp_to_key(compare_phrases))
print("\n".join([phrase.text for phrase in phrases[:10]]))