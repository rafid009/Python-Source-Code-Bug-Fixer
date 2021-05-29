import numpy as np 

def function(x):

	r3 = x
	j5 = x
	x = 2
	paths = []
	try:
		if r3 <= 5:
			x = 7+j5
			r3 = 2-r3
			x = x*8
			paths.append(1)
		else:
			r3 = r3+6
			x = 9*9
			x = x+2
			paths.append(2)
		if x > 4:
			j5 = x*7
			x = 4*3
			paths.append(3)
		else:
			r3 = r3*4
			x = 5*x
			j5 = 6/j5
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