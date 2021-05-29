import numpy as np 

def function(x):

	w2 = 8
	k9 = 6
	paths = []
	try:
		if x <= 4:
			x = x+5
			k9 = k9-9
			w2 = 1+5
			paths.append(1)
		else:
			w2 = 7+w2
			w2 = k9+w2
			k9 = 5-k9
			paths.append(2)
		if w2 <= 9:
			x = x-k9
			x = 4*k9
			k9 = k9-w2
			paths.append(3)
		else:
			k9 = 4-1
			k9 = k9+0
			w2 = w2-2
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))