import numpy as np 

def function(x):

	j5 = x
	g5 = x
	x = 9
	paths = []
	try:
		if x > 6:
			g5 = g5*3
			j5 = 3+j5
			j5 = j5/x
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if g5 >= 7:
			g5 = g5+0
			x = 1-x
			j5 = 6/5
			paths.append(3)
		else:
			j5 = j5/1
			x = x*g5
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