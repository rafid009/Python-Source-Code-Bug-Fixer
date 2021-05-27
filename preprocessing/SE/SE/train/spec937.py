import numpy as np 

def function(x):

	w6 = 5
	s2 = x
	paths = []
	try:
		if s2 < 9:
			x = x+s2
			w6 = w6-x
			w6 = w6*0
			paths.append(1)
		else:
			s2 = 2+s2
			x = x/s2
			x = x+0
			paths.append(2)
		if w6 > 9:
			w6 = w6/7
			s2 = x/5
			x = x/4
			paths.append(3)
		else:
			x = x/4
			s2 = x*8
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))