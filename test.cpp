#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

// 哈夫曼树节点结构
struct HuffmanNode {
    char ch;            // 字符
    int freq;           // 频率
    HuffmanNode *left;  // 左子节点
    HuffmanNode *right; // 右子节点
    
    HuffmanNode(char c, int f) : ch(c), freq(f), left(nullptr), right(nullptr) {}
};

// 用于优先队列的比较函数
struct Compare {
    bool operator()(HuffmanNode* a, HuffmanNode* b) {
        return a->freq > b->freq;
    }
};

// 统计字符频率
map<char, int> countCharacterFrequency(const string& text) {
    map<char, int> freqMap;
    for (char ch : text) {
        freqMap[ch]++;
    }
    return freqMap;
}

// 构建哈夫曼树
HuffmanNode* buildHuffmanTree(const map<char, int>& freqMap) {
    priority_queue<HuffmanNode*, vector<HuffmanNode*>, Compare> minHeap;
    
    // 为每个字符创建节点并加入最小堆
    for (auto pair : freqMap) {
        minHeap.push(new HuffmanNode(pair.first, pair.second));
    }
    
    // 构建哈夫曼树
    while (minHeap.size() > 1) {
        HuffmanNode* left = minHeap.top(); minHeap.pop();
        HuffmanNode* right = minHeap.top(); minHeap.pop();
        
        HuffmanNode* newNode = new HuffmanNode('\0', left->freq + right->freq);
        newNode->left = left;
        newNode->right = right;
        
        minHeap.push(newNode);
    }
    
    return minHeap.top();
}

// 生成哈夫曼编码表
void generateCodes(HuffmanNode* root, string code, map<char, string>& huffmanCode) {
    if (root == nullptr) return;
    
    // 叶子节点
    if (!root->left && !root->right) {
        huffmanCode[root->ch] = code;
    }
    
    generateCodes(root->left, code + "0", huffmanCode);
    generateCodes(root->right, code + "1", huffmanCode);
}

// 编码文本
string encodeText(const string& text, const map<char, string>& huffmanCode) {
    string encodedText;
    for (char ch : text) {
        encodedText += huffmanCode.at(ch);
    }
    return encodedText;
}

// 解码文本
string decodeText(HuffmanNode* root, const string& encodedText) {
    string decodedText;
    HuffmanNode* current = root;
    
    for (char bit : encodedText) {
        if (bit == '0') {
            current = current->left;
        } else {
            current = current->right;
        }
        
        // 到达叶子节点
        if (!current->left && !current->right) {
            decodedText += current->ch;
            current = root;
        }
    }
    
    // 检查是否有未完成的解码
    if (current != root) {
        decodedText += "\n[警告] 最后的代码子序列不能完全译码";
    }
    
    return decodedText;
}

// 打印字符频率
void printCharacterFrequency(const map<char, int>& freqMap) {
    cout << "字符频率统计:" << endl;
    for (auto pair : freqMap) {
        if (pair.first == ' ') {
            cout << "' ' (空格): " << pair.second << endl;
        } else if (pair.first == '\n') {
            cout << "'\\n' (换行): " << pair.second << endl;
        } else {
            cout << "'" << pair.first << "': " << pair.second << endl;
        }
    }
    cout << endl;
}

// 打印哈夫曼编码表
void printHuffmanCodes(const map<char, string>& huffmanCode) {
    cout << "哈夫曼编码表:" << endl;
    for (auto pair : huffmanCode) {
        if (pair.first == ' ') {
            cout << "' ' (空格): " << pair.second << endl;
        } else if (pair.first == '\n') {
            cout << "'\\n' (换行): " << pair.second << endl;
        } else {
            cout << "'" << pair.first << "': " << pair.second << endl;
        }
    }
    cout << endl;
}

int main() {
    string text;
    cout << "请输入文本: ";
    getline(cin, text);
    
    // 1. 统计字符频率
    map<char, int> freqMap = countCharacterFrequency(text);
    printCharacterFrequency(freqMap);
    
    // 2. 构建哈夫曼树
    HuffmanNode* huffmanTree = buildHuffmanTree(freqMap);
    
    // 3. 生成哈夫曼编码
    map<char, string> huffmanCode;
    generateCodes(huffmanTree, "", huffmanCode);
    printHuffmanCodes(huffmanCode);
    
    // 4. 编码文本
    string encodedText = encodeText(text, huffmanCode);
    cout << "编码后的文本: " << encodedText << endl << endl;
    
    // 5. 解码测试
    string codeToDecode;
    cout << "请输入要解码的二进制序列: ";
    cin >> codeToDecode;
    
    string decodedText = decodeText(huffmanTree, codeToDecode);
    cout << "解码后的文本: " << decodedText << endl;
    
    // 清理内存
    // 注意: 实际应用中应该实现树的销毁函数来递归删除所有节点
    // 这里为了简化省略了内存释放
    
    return 0;
}