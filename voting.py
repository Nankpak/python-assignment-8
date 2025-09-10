"""
TASK: Create a VotingSystem class.

Requirements:
1. The class should allow registering candidates.
2. Each candidate should start with 0 votes.
3. The class should allow voters (using voter IDs) to cast votes.
   - Ensure one voter cannot vote more than once.
4. Provide a method to display election results.

Example Usage:
    election = VotingSystem()
    election.register_candidate("Alice")
    election.register_candidate("Bob")
    election.vote("Voter1", "Alice")
    election.vote("Voter2", "Bob")
    election.vote("Voter3", "Alice")
    print(election.results())  # {"Alice": 2, "Bob": 1}
    print(election.winner()) # Alice
"""
class VotingSystem:
    def __init__(self):
        self.candidate = {'alice':0,'bob':0}
        self.voters = {}
    def registration(self,key,value):
        self.voters.update({key:value})
        print(self.voters)
    def voting(self,vote,name):
        self.vote = vote
        self.name = name
        if name in self.candidate:
            if self.vote and self.candidate['alice']:
                self.candidate['alice'] +=1
                print(self.candidate)
            else:
                self.vote and self.candidate['bob']
                self.candidate['bob'] +=1
                print(self.candidate)
        else:
            print('candidate those not exist')
    def result(self):
        print(f"The result of the election is ALICE vote {self.candidate['alice']}, and BOB vote {self.candidate['bob']}")
    def winner(self):
        if self.candidate['alice'] >  self.candidate['bob']:
            print('Alice is the winner')
        elif self.candidate['alice'] == self.candidate['bob']:
            print('it is a tide')
        else:
            print('Bob is the winner')
    
election = VotingSystem()
election.registration('nankpak','001')
election.voting('vote1','bob')
election.voting('vote','alic')
election.result()
election.winner()