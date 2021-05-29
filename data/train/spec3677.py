import numpy as np 

def function(x):

	u3 = 0
	j5 = x
	paths = []
	try:
		if j5 >= 3:
			u3 = u3*4
			paths.append(1)
		else:
			j5 = x+5
			paths.append(2)
		if j5 < 1:
			u3 = j5/x
			u3 = 2+u3
			u3 = u3*7
			paths.append(3)
		else:
			j5 = 5+j5
			j5 = j5/x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))