import numpy as np 

def function(x):

	j3 = x
	d6 = x
	paths = []
	try:
		if d6 <= 4:
			d6 = d6/4
			x = 6+x
			d6 = d6/1
			paths.append(1)
		else:
			x = x*2
			j3 = 8-j3
			paths.append(2)
		if j3 <= 8:
			x = j3/x
			x = 0-x
			paths.append(3)
		else:
			x = x/j3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		j3 = j3**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))