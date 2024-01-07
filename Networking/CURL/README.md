<h1>Welcome to the adventures of using CURL</h1>
<p>curl is  a tool for transferring data from or to a server. It supports these protocols: DICT, FILE, FTP, FTPS, GOPHER, GOPHERS,  HTTP,  HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET or TFTP. The command  is  designed to work without user interaction.

curl offers a busload of useful tricks like proxy support, user authentication, FTP upload, HTTP post, SSL connections, cookies, file transfer resume and more.</p>
<h4>Flags used when Working with requests</h4>
<ul>
<li>-X used to specify request method to use when communicating with the HTTP server. i.e: POST, PUT, OPTIONS, DELETE</li>
<li>-s,  --silent - Silent  or  quiet mode. Do not show progress meter or error messages. Makes Curl mute. It will still output the  data  you  ask for, potentially even to the terminal/stdout unless you redirect it.</li>
<li>-d used to add data to a POST request, in the same way that a browser does when a user has filled in an HTML form and presses the submit button</li>
<li>-H used to add a custom header</li>
<li>-I used to Fetch the request headers only</li>
<li>-i used to Include the HTTP response headers in the output</li>
<li>-K- Used to Specify a text file to read curl  arguments  from.  The  command line  arguments  found  in the text file will be used as if they were provided on the command line.</li>
<li>-b is used to Pass the data to the HTTP server in the Cookie header. Itis supposedly the data previously received from the server in  a "Set-Cookie:"   line.   The   data   should  be  in  the  format "NAME1=VALUE1; NAME2=VALUE2".</li>
<li>-f means Fail silently (no output at all) on server errors.</li>
<li>-F - this lets curl emulate a filled-in form in which a user  has  pressed  the  submit button. This causes curl to POST data using the Content-Type multipart/form-data in the format: name=content</li>
<li> -k - By default, every secure connection curl makes is verified to be secure before the transfer takes place. This  option  makes  curl skip the verification step and proceed without checking.
When this option is not used for protocols using TLS, curl verifies  the server's TLS certificate before it continues: that the certificate contains the right name which matches the host  name used in the URL and that the certificate has been signed by a CA certificate present in the cert store.</li>
<li>-L - If  the server reports that the requested page has moved(redirected) to a different location, this option will make curl redo the request on the new place. If used together with  -i,  --include  or  -I, --head, headers from all requested pages will be shown.</li>
<li>--max-filesize - Specify the maximum size (in bytes) of a file to download. If the file requested is larger than this  value, the transfer will not start</li>
<li>-o, --output - Write output to a file instead of stdout.</li>
<li>-#, --progress-bar - Make curl display transfer progress as a simple progress bar instead of the standard</li>
<li>--retry-all-errors - Retry on any error</li>
<li>-S, --show-error - When used with -s, --silent, it makes curl show an error message if it fails.</li>
<li>B, --use-ascii - Enable ASCII transfer.</li>
<li>-A, --user-agent (name) - Specify the User-Agent string to send to the HTTP server.</li>
<li>-u, --user (user:password) - Specify the user name and password to use for server authentication.</li>
<li>-v, --verbose - Makes  curl  verbose  during the operation. Useful for debugging and seeing what's going on "under the  hood".</li>
<li>-V, --version - Displays information about curl and the libcurl version it uses.</li>
<li>-w, --write-out (format)
Make curl display information on stdout after a completed transfer. The format is a string that may contain  plain  text  mixed with  any  number of variables.</li>
<li>-Y, --speed-limit (speed) - If a download is slower than this given speed (in bytes per second) for speed-time seconds it gets aborted.</li>
<li>-y, --speed-time (seconds)
If a download is slower than speed-limit bytes per second during a speed-time period, the download gets aborted.</li>
<li>--ssl-auto-client-cert - Tell libcurl to automatically locate and use a client certificate for authentication, when requested by the server.</li>
</ul>