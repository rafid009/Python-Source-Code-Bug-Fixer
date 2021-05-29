import numpy as np 

def function(x):

	j7 = 5
	u3 = 4
	paths = []
	try:
		if x < 6:
			u3 = u3*u3
			u3 = 5-u3
			x = 2-x
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if u3 < 4:
			u3 = u3/3
			j7 = j7-7
			j7 = 9+x
			paths.append(3)
		else:
			u3 = 1-u3
			j7 = u3/x
			x = u3/9
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		j7 = u3**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))