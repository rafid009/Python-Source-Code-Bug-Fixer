import numpy as np 

def function(x):

	r1 = x
	j5 = 1
	paths = []
	try:
		if j5 <= 5:
			r1 = 6+r1
			j5 = r1*9
			x = j5-r1
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if x < 3:
			j5 = 9/x
			x = x*j5
			x = x/1
			paths.append(3)
		else:
			j5 = 6+j5
			r1 = 7/r1
			j5 = 0-j5
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		j5 = r1**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))