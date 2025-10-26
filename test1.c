#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// 定义单词类型
typedef enum {
    ID, NUM, PLUS, MINUS, STAR, DIV, ASSIGN, LPAREN, RPAREN, 
    SEMICOLON, BEGIN, END, HASH, ERROR
} TokenType;

// 全局变量：当前单词和输入缓冲区
TokenType current_token;
char token_str[20];
char input[1000];
int pos = 0;

// 从输入中读取下一个单词
void get_next_token() {
    // 跳过空白字符
    while (input[pos] != '\0' && isspace(input[pos])) {
        pos++;
    }
    
    if (input[pos] == '\0') {
        current_token = ERROR;
        return;
    }
    
    // 识别标识符或关键字
    if (isalpha(input[pos])) {
        int i = 0;
        while (isalnum(input[pos])) {
            token_str[i++] = input[pos++];
        }
        token_str[i] = '\0';
        
        if (strcmp(token_str, "begin") == 0) {
            current_token = BEGIN;
        } else if (strcmp(token_str, "end") == 0) {
            current_token = END;
        } else {
            current_token = ID;
        }
        return;
    }
    
    // 识别数字
    if (isdigit(input[pos])) {
        int i = 0;
        while (isdigit(input[pos])) {
            token_str[i++] = input[pos++];
        }
        token_str[i] = '\0';
        current_token = NUM;
        return;
    }
    
    // 识别运算符和分隔符
    switch (input[pos]) {
        case '+':
            current_token = PLUS;
            pos++;
            break;
        case '-':
            current_token = MINUS;
            pos++;
            break;
        case '*':
            current_token = STAR;
            pos++;
            break;
        case '/':
            current_token = DIV;
            pos++;
            break;
        case '(':
            current_token = LPAREN;
            pos++;
            break;
        case ')':
            current_token = RPAREN;
            pos++;
            break;
        case ';':
            current_token = SEMICOLON;
            pos++;
            break;
        case '#':
            current_token = HASH;
            pos++;
            break;
        case ':':
            // 处理赋值符号 :=
            if (input[pos+1] == '=') {
                current_token = ASSIGN;
                pos += 2;
            } else {
                current_token = ERROR;
                pos++;
            }
            break;
        default:
            current_token = ERROR;
            pos++;
    }
}

// 递归下降分析函数声明
void program();
void statement_list();
void statement();
void assignment_statement();
void expression();
void term();
void factor();

// 错误处理函数
void error() {
    printf("error\n");
    exit(0);
}

// 〈程序〉::= begin〈语句串〉end
void program() {
    if (current_token == BEGIN) {
        get_next_token();
        statement_list();
        if (current_token == END) {
            get_next_token();
            return;
        }
    }
    error();
}

// 〈语句串〉::= 〈语句〉|〈语句〉;〈语句串〉
void statement_list() {
    statement();
    while (current_token == SEMICOLON) {
        get_next_token();
        statement();
    }
}

// 〈语句〉::= 〈赋值语句〉
void statement() {
    assignment_statement();
}

// 〈赋值语句〉::= ID:=〈表达式〉
void assignment_statement() {
    if (current_token == ID) {
        get_next_token();
        if (current_token == ASSIGN) {
            get_next_token();
            expression();
            return;
        }
    }
    error();
}

// 修正表达式定义：〈表达式〉::= 〈项〉|〈表达式〉+〈项〉|〈表达式〉-〈项〉
// 支持多个加法/减法运算（如 a + b - c）
void expression() {
    term();
    while (current_token == PLUS || current_token == MINUS) {
        get_next_token();
        term();
    }
}

// 〈项〉::= 〈因子〉|〈项〉*〈因子〉|〈项〉/〈因子〉
void term() {
    factor();
    while (current_token == STAR || current_token == DIV) {
        get_next_token();
        factor();
    }
}

// 〈因子〉::= ID|NUM|（〈表达式〉）
void factor() {
    switch (current_token) {
        case ID:
            get_next_token();
            break;
        case NUM:
            get_next_token();
            break;
        case LPAREN:
            get_next_token();
            expression();
            if (current_token == RPAREN) {
                get_next_token();
                break;
            }
            error();
        default:
            error();
    }
}

int main() {
   
    fgets(input, sizeof(input), stdin);
    // 去除输入中的换行符
    input[strcspn(input, "\n")] = '\0';
    
    get_next_token();
    program();
    
    // 检查是否以#结束且没有多余字符
    if (current_token == HASH) {
        get_next_token();
        if (current_token == ERROR) {
            printf("success\n");
        } else {
            error();
        }
    } else {
        error();
    }
    
    return 0;
}