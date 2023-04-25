#Number Of Substrings Containing All Three Characters
<p>Given a string <code>s</code> consisting only of characters <em>a</em>, <em>b</em> and <em>c</em>.</p>
<p>Return the number of substrings containing <b>at least</b> one occurrence of all these characters <em>a</em>, <em>b</em> and <em>c</em>.</p>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcabc"
<strong>Output:</strong> 10
<strong>Explanation:</strong> The substrings containing at least one occurrence of the characters <em>a</em>, <em>b</em> and <em>c are "</em>abc<em>", "</em>abca<em>", "</em>abcab<em>", "</em>abcabc<em>", "</em>bca<em>", "</em>bcab<em>", "</em>bcabc<em>", "</em>cab<em>", "</em>cabc<em>" </em>and<em> "</em>abc<em>" </em>(<strong>again</strong>)<em>. </em>
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "aaacb"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substrings containing at least one occurrence of the characters <em>a</em>, <em>b</em> and <em>c are "</em>aaacb<em>", "</em>aacb<em>" </em>and<em> "</em>acb<em>".</em><em> </em>
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "abc"
<strong>Output:</strong> 1
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>3 &lt;= s.length &lt;= 5 x 10^4</code></li>
<li><code>s</code> only consists of <em>a</em>, <em>b</em> or <em>c </em>characters.</li>
</ul>
