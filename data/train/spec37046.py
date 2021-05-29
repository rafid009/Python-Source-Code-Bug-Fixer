import numpy as np 

def function(x):

	w2 = x
	s1 = x
	paths = []
	try:
		if w2 <= 6:
			w2 = 3/w2
			x = 5/x
			paths.append(1)
		else:
			x = x*w2
			paths.append(2)
		if w2 < 9:
			x = 5+x
			s1 = 4-s1
			w2 = w2*s1
			paths.append(3)
		else:
			w2 = w2*2
			w2 = s1+2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		s1 = w2**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))