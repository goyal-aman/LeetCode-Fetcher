#Counter
<p>Given an integer <code>n</code>, return a <code>counter</code> function. This <code>counter</code> function initially returns <code>n</code> and then returns 1 more than the previous value every subsequent time it is called (<code>n</code>, <code>n + 1</code>, <code>n + 2</code>, etc).</p>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> 
n = 10 
["call","call","call"]
<strong>Output:</strong> [10,11,12]
<strong>Explanation: 
</strong>counter() = 10 // The first time counter() is called, it returns n.
counter() = 11 // Returns 1 more than the previous time.
counter() = 12 // Returns 1 more than the previous time.
</pre>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> 
n = -2
["call","call","call","call","call"]
<strong>Output:</strong> [-2,-1,0,1,2]
<strong>Explanation:</strong> counter() initially returns -2. Then increases after each sebsequent call.
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>-1000<sup> </sup>&lt;= n &lt;= 1000</code></li>
<li><code>At most 1000 calls to counter() will be made</code></li>
</ul>