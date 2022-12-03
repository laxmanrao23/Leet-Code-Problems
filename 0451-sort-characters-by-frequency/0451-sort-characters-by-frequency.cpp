class Solution {
public:
    static bool cmp(pair<char,int>&a, pair<char, int>&b){
        
        if(a.second > b.second)
            return true;
        return false;
    }
    string frequencySort(string s) {
        
        unordered_map<char, int>ch;
        for(int i=0; i<s.length(); i++){
            ch[s[i]]++;
        }
        vector<pair<char, int> > vp(ch.begin(), ch.end());
        sort(vp.begin(), vp.end(), cmp);
        
        string str = "";
        for(int i=0; i<vp.size(); i++)
        {
            pair<char, int> p = vp[i];
            while(p.second > 0){
                str.push_back(p.first);
                p.second-- ;
            }
        }
        return str;
    }
};