#Find The Divisibility Array Of A String
<p>You are given a <strong>0-indexed</strong> string <code>word</code> of length <code>n</code> consisting of digits, and a positive integer <code>m</code>.</p>
<p>The <strong>divisibility array</strong> <code>div</code> of <code>word</code> is an integer array of length <code>n</code> such that:</p>
<ul>
<li><code>div[i] = 1</code> if the <strong>numeric value</strong> of <code>word[0,...,i]</code> is divisible by <code>m</code>, or</li>
<li><code>div[i] = 0</code> otherwise.</li>
</ul>
<p>Return<em> the divisibility array of</em><em> </em><code>word</code>.</p>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> word = "998244353", m = 3
<strong>Output:</strong> [1,1,0,0,0,1,1,0,0]
<strong>Explanation:</strong> There are only 4 prefixes that are divisible by 3: "9", "99", "998244", and "9982443".
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> word = "1010", m = 10
<strong>Output:</strong> [0,1,0,1]
<strong>Explanation:</strong> There are only 2 prefixes that are divisible by 10: "10", and "1010".
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
<li><code><font face="monospace">word.length == n</font></code></li>
<li><code><font face="monospace">word</font></code><font face="monospace"> consists of digits from <code>0</code> to <code>9</code></font></li>
<li><code><font face="monospace">1 &lt;= m &lt;= 10<sup>9</sup></font></code></li>
</ul>
