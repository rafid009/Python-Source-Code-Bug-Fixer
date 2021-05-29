import numpy as np 

def function(x):

	j3 = x
	n4 = x
	paths = []
	try:
		if n4 > 9:
			j3 = 3/5
			x = 2+x
			j3 = j3/2
			paths.append(1)
		else:
			n4 = 0+0
			j3 = j3+3
			paths.append(2)
		if j3 <= 3:
			n4 = n4*7
			j3 = 4+j3
			x = 6-x
			paths.append(3)
		else:
			j3 = j3*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))