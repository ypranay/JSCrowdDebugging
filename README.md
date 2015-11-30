# JSCrowdDebugging
##Step 1:
Fetch top 50,000 Q&A posts pertaining to JavaScript from StackExchange. Check. (Available in a file - query.csv)
##Step 2:
Find out relevant Q&A code pairs which can be used for Crowd Debugging. Following are my assumptions-
  1. Out of the many <code> </code> separated texts in the posts, choose the one of the maximum length. Higher chance of being relevant.
  2. If a post contains only text and no code snippets, silently ignore.
##Step 3:
Output the code snippets for Q&A in separate JS files, IDed by the Question and Answer post IDs from which they were extracted.
##Step 4: 
Randomly choose 10 of the code snippets from the folder containing the question JS files. Tweak them to some extent and use this as a test set for testing if the code clone matching works fine.
##Step 5: 
For each of the tweaked JS file (target question snippet), take a note of the question JS file from which it originated (parent question snippet). This will later be used for evaluation.
##Step 6:
Using jsinspect, find code clones for the target question snippet for decreasing values of threshold (init- 30) and record if the parent code snippet is mentioned as a code clone for that particular threshold.
##Step 7:
Identify which value of the threshold gives the best results (more cases where the target question snippet gave closest similarity to parent question snippet)
##Step 8:
We can now use this method to suggest answer code snippets, pertaining to the parent question snippet as a crowd debugging solution for the target question snippet.
