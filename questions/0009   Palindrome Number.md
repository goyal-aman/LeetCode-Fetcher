#Palindrome Number
<p>Given an integer <code>x</code>, return <code>true</code><em> if </em><code>x</code><em> is a </em><span class="cursor-pointer relative text-dark-blue-s text-sm" data-keyword="palindrome-integer"><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div aria-expanded="false" data-headlessui-state="" id="headlessui-popover-button-:Rg3369j9l5t6:"><em><strong>palindrome</strong></em></div></div></div></span><em>, and </em><code>false</code><em> otherwise</em>.</p>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>
<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
<p> </p>
<strong>Follow up:</strong> Could you solve it without converting the integer to a string?
