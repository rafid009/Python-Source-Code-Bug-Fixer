import numpy as np 

def function(x):

	w7 = x
	s5 = x
	paths = []
	try:
		if x < 2:
			x = 2-5
			s5 = 2+w7
			paths.append(1)
		else:
			w7 = w7/1
			s5 = s5/9
			paths.append(2)
		if x >= 3:
			w7 = w7+5
			w7 = x-w7
			paths.append(3)
		else:
			s5 = 9/s5
			x = 5-x
			s5 = s5-3
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		w7 = s5**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))