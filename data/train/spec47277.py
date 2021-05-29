import numpy as np 

def function(x):

	j5 = x
	r7 = 4
	paths = []
	try:
		if x < 2:
			j5 = 7*5
			paths.append(1)
		else:
			r7 = 2-r7
			paths.append(2)
		if r7 <= 5:
			j5 = j5+1
			paths.append(3)
		else:
			j5 = x+8
			r7 = r7+0
			r7 = 1/4
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))