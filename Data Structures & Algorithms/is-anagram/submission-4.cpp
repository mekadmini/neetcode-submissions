class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()) return false;
        std::unordered_map<char, int> saved;
        for (char e: s){
            saved[e]++;

        }

        for (char e: t){
            saved[e]--;

        }

        for (auto& [character, frequency] : saved){
            if (frequency != 0) return false; 

        }
        return true;
        
    }
};
