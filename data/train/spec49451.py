import numpy as np 

def function(x):

	l5 = x
	w5 = x
	paths = []
	try:
		if w5 > 5:
			w5 = l5*9
			x = x+7
			w5 = w5*5
			paths.append(1)
		else:
			l5 = 3-8
			x = x/4
			w5 = w5*2
			paths.append(2)
		if l5 > 7:
			x = 3+7
			paths.append(3)
		else:
			w5 = w5-0
			x = 7+x
			l5 = 0-x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		l5 = w5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))