import numpy as np 

def function(x):

	s9 = x
	v5 = 0
	x = 6
	paths = []
	try:
		if v5 < 9:
			x = x+2
			v5 = 0+s9
			paths.append(1)
		else:
			v5 = v5*s9
			paths.append(2)
		if v5 > 2:
			x = 2-0
			s9 = 6+s9
			x = x/8
			paths.append(3)
		else:
			s9 = s9+x
			x = s9*0
			s9 = s9/9
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))