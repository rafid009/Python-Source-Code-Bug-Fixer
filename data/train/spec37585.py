import numpy as np 

def function(x):

	j2 = 5
	t1 = x
	x = 2
	paths = []
	try:
		if t1 < 3:
			j2 = 8-j2
			j2 = t1/3
			x = 4/x
			paths.append(1)
		else:
			x = 3*x
			j2 = x*8
			paths.append(2)
		if x < 8:
			j2 = 4/6
			paths.append(3)
		else:
			j2 = 5/j2
			t1 = t1+t1
			t1 = 4+0
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		j2 = t1**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))