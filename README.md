<h1>
    Introduction
</h1>
<p>
    Script is used to download and generate statistics for Debian packages for a certain
    architecture. Debian mirror link via  http://ftp.uk.debian.org/debian/dists/stable/main/
</p>
<h1>
    Usage
</h1>
<p>
    Use <code>./package_statistics.py &lt;architecture-name&gt;</code> to run. System must have Python3.6 or higher via 
    <code>python3</code>.
</p>
<h1>
    Design process
</h1>
<ol>
    <li>Program requires an input parser. In Python, the module <i>argparse</i> provides
    a very robust solution for this.</li>
    <li>Construct the url for the gz file using the aforementioned Debian mirror</li>
    <li>Download the url via <i>urllib.request</i> module and load into memory</li>
    <li>Perform string manipulation to generate a hashmap for statistics</li>
    <li>Output and format the result</li>
</ol>
<h1>
    Time taken to completed
</h1>
<p>
    Approximately 3 hours. By 
</p>
<p>
Danh Nguyen, 2023</p>