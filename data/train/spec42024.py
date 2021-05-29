import numpy as np 

def function(x):

	k9 = x
	s5 = x
	x = x
	paths = []
	try:
		if x <= 5:
			x = x*8
			k9 = k9+1
			s5 = s5-k9
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if x <= 0:
			x = 8*x
			paths.append(3)
		else:
			x = 0/x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		k9 = s5**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))