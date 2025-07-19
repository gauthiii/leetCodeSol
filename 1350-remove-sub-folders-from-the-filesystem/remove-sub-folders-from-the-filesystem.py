class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders alphabetically
        folder.sort()
        result = []
        
        # Iterate through the sorted folder list
        for f in folder:
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result