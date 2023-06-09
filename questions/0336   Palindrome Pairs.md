#Palindrome Pairs
<p>You are given a <strong>0-indexed</strong> array of <strong>unique</strong> strings <code>words</code>.</p>
<p>A <strong>palindrome pair</strong> is a pair of integers <code>(i, j)</code> such that:</p>
<ul>
<li><code>0 &lt;= i, j &lt; words.length</code>,</li>
<li><code>i != j</code>, and</li>
<li><code>words[i] + words[j]</code> (the concatenation of the two strings) is a <span class="cursor-pointer relative text-dark-blue-s text-sm" data-keyword="palindrome-string"><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:R1sb369j9l5t6:">palindrome</div></div></div></span>.</li>
</ul>
<p>Return <em>an array of all the <strong>palindrome pairs</strong> of </em><code>words</code>.</p>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> words = ["abcd","dcba","lls","s","sssll"]
<strong>Output:</strong> [[0,1],[1,0],[3,2],[2,4]]
<strong>Explanation:</strong> The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> words = ["bat","tab","cat"]
<strong>Output:</strong> [[0,1],[1,0]]
<strong>Explanation:</strong> The palindromes are ["battab","tabbat"]
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> words = ["a",""]
<strong>Output:</strong> [[0,1],[1,0]]
<strong>Explanation:</strong> The palindromes are ["a","a"]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= words.length &lt;= 5000</code></li>
<li><code>0 &lt;= words[i].length &lt;= 300</code></li>
<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>
