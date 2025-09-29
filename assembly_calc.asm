section .data
    msg db "Hello", 0xA  ; The message with newline character
    len equ $ - msg      ; Length of the message

section .text
    global _start

_start:
    ; write syscall: write(1, msg, len)
    mov eax, 4          ; syscall number for sys_write
    mov ebx, 1          ; file descriptor 1 is stdout
    mov ecx, msg        ; pointer to message
    mov edx, len        ; message length
    int 0x
