import numpy as np 

def function(x):

	u1 = 8
	j5 = 1
	paths = []
	try:
		if u1 < 4:
			x = j5/x
			j5 = j5+8
			j5 = j5/3
			paths.append(1)
		else:
			u1 = u1*4
			j5 = j5*5
			j5 = 6/j5
			paths.append(2)
		if x > 9:
			x = x+3
			j5 = j5/5
			paths.append(3)
		else:
			x = x*4
			x = x+3
			j5 = j5+x
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