import numpy as np 

def function(x):

	w2 = 2
	s7 = 9
	x = x
	paths = []
	try:
		if x > 2:
			s7 = w2+w2
			w2 = s7-2
			paths.append(1)
		else:
			w2 = w2+x
			x = x*9
			x = w2+x
			paths.append(2)
		if s7 <= 3:
			w2 = w2/w2
			paths.append(3)
		else:
			w2 = w2/4
			s7 = s7/1
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		w2 = w2**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))