About the Project: 
What is a Buffer Overflow Attack​?

Attackers use programme memory overwriting to take advantage of buffer overflow vulnerabilities. By altering the program's execution path, this can cause reactions that corrupt files or reveal sensitive information. ​

For instance, to access IT systems, a hacker can add more code and send the application brand-new instructions.​

If an attacker is aware of a program's memory layout, they can purposefully input data that the buffer is not designed to hold. They can even rewrite regions that contain executable code with their own code. ​

For instance, to take control of the application, an attacker could rewrite a pointer—an object that points to another location in memory—and direct it to the exploit payload.​


Project Working and Setup:
- Compile the code using `make`. It will generate two executables:
  `a32.out` (32-bit code) and `a64.out` (64-bit code).

- Run the two Python programs to generate the shellcode, one for 32-bit,
  and the other for 64-bit. You can modify the shellcode.  

- Run `a32.out` and `a64.out` to test your shellcode.

Contributors:
Devanshi Shah
Darshil Shah
