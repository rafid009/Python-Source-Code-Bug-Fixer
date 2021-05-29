import numpy as np 

def function(x):

	i9 = 9
	u3 = x
	paths = []
	try:
		if i9 < 0:
			u3 = 1*u3
			paths.append(1)
		else:
			u3 = u3+9
			paths.append(2)
		if u3 > 5:
			u3 = u3/1
			i9 = u3/i9
			paths.append(3)
		else:
			i9 = 4*x
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))