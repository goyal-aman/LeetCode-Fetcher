#Memoize
<p>Given a function <code>fn</code>, return a <strong>memoized</strong> version of that function.</p>
<p>A <strong>memoized </strong>function is a function that will never be called twice with the same inputs. Instead it will return a cached value.</p>
<p>You can assume there are <strong>3 </strong>possible input functions: <code>sum</code><strong>, </strong><code>fib</code><strong>, </strong>and <code>factorial</code><strong>.</strong></p>
<ul>
<li><code>sum</code><strong> </strong>accepts two integers <code>a</code> and <code>b</code> and returns <code>a + b</code>.</li>
<li><code>fib</code><strong> </strong>accepts a single integer <code>n</code> and returns <code>1</code> if <font face="monospace"><code>n &lt;= 1</code> </font>or<font face="monospace"> <code>fib(n - 1) + fib(n - 2)</code> </font>otherwise.</li>
<li><code>factorial</code> accepts a single integer <code>n</code> and returns <code>1</code> if <code>n &lt;= 1</code> or <code>factorial(n - 1) * n</code> otherwise.</li>
</ul>
<p> </p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
"sum"
["call","call","getCallCount","call","getCallCount"]
[[2,2],[2,2],[],[1,2],[]]
<strong>Output</strong>
[4,4,1,3,2]
<p><strong>Explanation</strong>
const sum = (a, b) =&gt; a + b;
const memoizedSum = memoize(sum);
memoizedSum(2, 2); // Returns 4. sum() was called as (2, 2) was not seen before.
memoizedSum(2, 2); // Returns 4. However sum() was not called because the same inputs were seen before.
// Total call count: 1
memoizedSum(1, 2); // Returns 3. sum() was called as (1, 2) was not seen before.
// Total call count: 2
</pre></p>
<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input
</strong>"factorial"
["call","call","call","getCallCount","call","getCallCount"]
[[2],[3],[2],[],[3],[]]
<strong>Output</strong>
[2,6,2,2,6,2]
<p><strong>Explanation</strong>
const factorial = (n) =&gt; (n &lt;= 1) ? 1 : (n * factorial(n - 1));
const memoFactorial = memoize(factorial);
memoFactorial(2); // Returns 2.
memoFactorial(3); // Returns 6.
memoFactorial(2); // Returns 2. However factorial was not called because 2 was seen before.
// Total call count: 2
memoFactorial(3); // Returns 6. However factorial was not called because 3 was seen before.
// Total call count: 2
</pre></p>
<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input
</strong>"fib"
["call","getCallCount"]
[[5],[]]
<strong>Output</strong>
[8,1]
<p><strong>Explanation
</strong>fib(5) = 8
// Total call count: 1</p>
<p></pre></p>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>0 &lt;= a, b &lt;= 10<sup>5</sup></code></li>
<li><code>1 &lt;= n &lt;= 10</code></li>
<li><code>at most 10<sup>5</sup> function calls</code></li>
<li><code>at most 10<sup>5</sup> attempts to access callCount</code></li>
<li><code>input function is sum, fib, or factorial</code></li>
</ul>
