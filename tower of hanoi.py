class Solution:
    def toh(self, N, fromm, to, aux):
        # Base case: if there is only one disk to move, move it directly from 'fromm' to 'to'
        if N == 1:
            print("Move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            print("\n")
            return 1
        
        # Recursive case: move N-1 disks from 'fromm' to 'aux', using 'to' as a checkpoint
        moves = 0
        moves += self.toh(N-1, fromm, aux, to)  # recursive call
        moves += 1  # increment the total moves count for the current step
        
        # Move the remaining largest disk from 'fromm' to 'to'
        print("Move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        
        # Recursive call: now move the N-1 disks from 'aux' to 'to' using 'fromm' as a checkpoint
        moves += self.toh(N-1, aux, to, fromm)
        return moves

# Example usage:
s = Solution()
print(s.toh(3, 1, 3, 2))