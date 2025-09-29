section .data
msg_add db "Addition result: ",0
msg_mul db "Multiplication result: ",0
newline db 10,0
section .bss
section .text
global _start
_start:
mov eax,10
mov ebx,5
add eax,ebx
mov ecx,eax
mov edx,msg_add
mov eax,4
mov ebx,1
mov ecx,msg_add
mov edx,18
int 0x80
mov eax,ecx
add eax,'0'
mov [msg_add+17],al
mov edx,18
mov ecx,msg_add
mov eax,4
mov ebx,1
int 0x80
mov eax,4
mov ebx,1
mov ecx,newline
mov edx,1
int 0x80
mov eax,10
mov ebx,5
mul ebx
mov ecx,eax
mov edx,msg_mul
mov eax,4
mov ebx,1
mov ecx,msg_mul
mov edx,22
int 0x80
mov eax,ecx
add eax,'0'
mov [msg_mul+21],al
mov edx,22
mov ecx,msg_mul
mov eax,4
mov ebx,1
int 0x80
mov eax,4
mov ebx,1
mov ecx,newline
mov edx,1
int 0x80
mov eax,1
xor ebx,ebx
int 0x80

