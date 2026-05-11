
/*

Alg.
1. maintain 2 pointers which keeps track of the current window (sliding window), start at 0 and 1
2. maintain a current max, were just looking for the number so we dont need to maintain the actually substring
3. maintain some dictionary like structure to maintain what has been seen already

*/ 


class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        // maintain a constant sized structure, can be bools since we are only maintain
        // one occurrence, we can mark "seen" vs. "not seen", in substring
        std::unordered_set<char> dict;

        int curr_max = 0;

        // initialize pointers
        int i = 0;
        int j = 0;

        while (j < s.size()) {

            // int char_index = static_cast<int>(s[j]);
            std::cout << i << ", " << j << std::endl;
            
            auto it = dict.find(s[j]);
            if (it != dict.end()) {
                dict.erase(s[i++]);
            }
            else {
                dict.insert(s[j++]);
            }

            curr_max = curr_max > (j - i) ? curr_max : (j - i);

        }

        return curr_max;
        
    }
};
