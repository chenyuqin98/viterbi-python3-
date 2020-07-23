###########################################################################################################
# Viterbi Algorithm for HMM
# dynamic programming, time complexity O(mn^2), m is the length of sequence of observation, n is the number of hidden states
##########################################################################################################


# five elements for HMM
states = ('Healthy', 'Fever')

observations = ('normal', 'cold', 'dizzy')

start_probability = {'Healthy': 0.6, 'Fever': 0.4}

transition_probability = {
    'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
    'Fever': {'Healthy': 0.4, 'Fever': 0.6},
}

emission_probability = {
    'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
}


def Viterbi(obs):
    path={s:[] for s in states}
    curr_pro={}
    for s in states:
        curr_pro[s]=start_probability[s]*emission_probability[s][obs[0]]
    for i in range(1,len(obs)):
        last_pro=curr_pro
        curr_pro={}
        for curr in states:
            max_pro,last_state=max(
                (last_pro[last]*transition_probability[last][curr]*emission_probability[curr][obs[i]],last)
                for last in states)
            curr_pro[curr]=max_pro
            path[curr].append(last_state)
    final_pro=-1
    max_path=None
    for s in states:
        path[s].append(s)
        if curr_pro[s]>final_pro:
            max_path=path[s]
            final_pro=curr_pro[s]
    return max_path



if __name__ == '__main__':
    obs = ['normal', 'cold', 'dizzy']
    print((Viterbi(obs)))


