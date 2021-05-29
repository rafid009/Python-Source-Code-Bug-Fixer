import numpy as np 

def function(x):

	k9 = 6
	s4 = x
	x = 6
	paths = []
	try:
		if k9 >= 3:
			k9 = 3*s4
			x = x*s4
			k9 = 5+s4
			paths.append(1)
		else:
			k9 = k9*x
			s4 = s4*0
			paths.append(2)
		if k9 >= 8:
			k9 = 8+3
			x = x/5
			k9 = 7*k9
			paths.append(3)
		else:
			k9 = 7/k9
			s4 = s4*s4
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))