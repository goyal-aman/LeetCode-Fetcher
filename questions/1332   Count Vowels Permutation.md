#Count Vowels Permutation
<p>Given an integer <code>n</code>, your task is to count how many strings of length <code>n</code> can be formed under the following rules:</p>
<ul>
<li>Each character is a lower case vowel (<code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, <code>'u'</code>)</li>
<li>Each vowel <code>'a'</code> may only be followed by an <code>'e'</code>.</li>
<li>Each vowel <code>'e'</code> may only be followed by an <code>'a'</code> or an <code>'i'</code>.</li>
<li>Each vowel <code>'i'</code> <strong>may not</strong> be followed by another <code>'i'</code>.</li>
<li>Each vowel <code>'o'</code> may only be followed by an <code>'i'</code> or a <code>'u'</code>.</li>
<li>Each vowel <code>'u'</code> may only be followed by an <code>'a'.</code></li>
</ul>
<p>Since the answer may be too large, return it modulo <code>10^9 + 7.</code></p>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> All possible strings are: "a", "e", "i" , "o" and "u".
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 10
<strong>Explanation:</strong> All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
</pre>
<p><strong class="example">Example 3: </strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> 68</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= n &lt;= 2 * 10^4</code></li>
</ul>
