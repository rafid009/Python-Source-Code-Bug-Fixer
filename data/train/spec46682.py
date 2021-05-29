import numpy as np 

def function(x):

	u1 = x
	j6 = 0
	x = x
	paths = []
	try:
		if j6 < 1:
			j6 = j6+u1
			x = 7-4
			paths.append(1)
		else:
			j6 = 4+j6
			x = x*0
			paths.append(2)
		if x <= 0:
			j6 = 2/x
			j6 = 6+x
			paths.append(3)
		else:
			u1 = u1+7
			j6 = j6-8
			x = x+2
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		j6 = u1**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))