import numpy as np 

def function(x):

	w9 = 3
	p9 = 1
	paths = []
	try:
		if x < 0:
			x = w9*0
			x = x-p9
			paths.append(1)
		else:
			p9 = 7/w9
			paths.append(2)
		if w9 > 4:
			x = 7*3
			x = x-w9
			w9 = w9*w9
			paths.append(3)
		else:
			p9 = p9/x
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		w9 = p9**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))