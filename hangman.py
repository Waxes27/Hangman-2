import random


def read_file(file_name):
    o_file = open(file_name,'r')
    words = o_file.readlines()
    o_file.close()
    return words


def get_user_input(answer):
	return input("Guess the missing letter: ")


def ask_file_name():
	file_name = "short_words.txt"
	file_name = input("Words file? [leave empty to use short_words.txt] : ")
	if not file_name:
		return 'short_words.txt'
	return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


#Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
	x = random.randint(0, len(word)-1)
	guessed = word.find(word[x])
	letter = word[x]
	u_word = list(word.replace(word, "_"*len(word)))
	u_word[guessed] = letter
	u_word = "".join(u_word)

	return u_word
	


#Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
	"""guessed = original_word.find(char)
	#print(original_word[guessed])
	#print(list(answer_word))
	answer_word = list(answer_word)

	if guessed != -1:
		return True
#	else:
#		print(original_word[guessed] + " " + char)
	"""
	if char in original_word and char not in answer_word:
		return True
	return False

#Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
	"""
	print(original_word)
	print(answer_word)
	print(char)
	for letter in original_word:
		if letter == "_" or letter == char:
			guessed = original_word.find(char)

			answer_word = list(answer_word)

			answer_word[guessed] = original_word[guessed]
			#print("".join(answer_word))
		#else:
			#print("nope")
	"""	
	for j in range(len(original_word)):
		if answer_word[j] == "_" and original_word[j] == char:
			answer_word = answer_word.replace(answer_word[j], char,1)
	return answer_word
	#return "".join(answer_word)
	
	

def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    #print(answer)
    return answer


#Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
	print('Wrong! Number of guesses left: '+str(number_guesses))
	number_guesses -= 1
	draw_figure(number_guesses)
	return number_guesses
	


#Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    if number_guesses == 4:
        print("/"+"-"*4)
        print("|\n"*3+"|")
        print("_"*7)    
    elif number_guesses == 3:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|\n"*3)
        print("_"*7)
    elif number_guesses == 2:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|"+" "*2+"/"+" "+"\\")
        print("|\n"*2)
        print("_"*7)
    elif number_guesses == 1:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|"+" "*2+"/|" +"\\")
        print("|"+" "*3 +"|")
        print("|")
        print("_"*7)
    elif number_guesses == 0:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|"+" "*2+"/|"+"\\")
        print("|"+" "*3 +"|")
        print("|"+" "*2+"/ " +"\\")
        print("_"*7)
"""
Step 2 - update to loop over getting input and checking until whole word guessed
Step 3 - update loop to exit game if user types `exit` or `quit`
Step 4 - keep track of number of remaining guesses
"""
def run_game_loop(word, answer):#,number_guesses):
	i = 0
	number_guesses = 4
	print("Guess the word: " +answer)
	while number_guesses >= 0:
		
		guess = get_user_input(answer)		#done
		
		if guess == "quit" or guess == "exit":
			print("Bye!")
			return 0
		if is_missing_char(word, answer, guess):
	
			answer = do_correct_answer(word, answer, guess)
			print(answer.strip("\n"))
			if word == answer:
				#print("Guess the missing letter: "+answer +"\n")
				return 0;
			#else:
				return do_correct_answer(word,answer,guess)#, run_game_loop(word, answer)
			
		else:
			
			number_guesses = do_wrong_answer(answer, number_guesses)
	print("Sorry, you are out of guesses. The word was: "+ word)


#Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()			#done
    words = read_file(words_file)			#done
    selected_word = select_random_word(words)		#done
    current_answer = random_fill_word(selected_word)	#done

    #print("Guess the word: "+current_answer)
    run_game_loop(selected_word, current_answer)

