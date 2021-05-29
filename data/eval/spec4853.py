import numpy as np 

def function(x):

	d5 = 9
	j6 = x
	x = 6
	paths = []
	try:
		if d5 <= 5:
			x = x-8
			x = x-4
			x = x*1
			paths.append(1)
		else:
			d5 = 2*8
			paths.append(2)
		if j6 <= 7:
			j6 = 2-3
			d5 = 0-d5
			d5 = 7*d5
			paths.append(3)
		else:
			j6 = x-j6
			d5 = 3/d5
			d5 = d5*0
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))