import numpy as np 

def function(x):

	i1 = x
	u3 = x
	paths = []
	try:
		if i1 >= 9:
			i1 = i1+0
			paths.append(1)
		else:
			x = u3+0
			u3 = 9/u3
			x = i1*0
			paths.append(2)
		if u3 > 0:
			x = 6+x
			i1 = 7*i1
			x = 6/7
			paths.append(3)
		else:
			x = u3*x
			i1 = u3+i1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		u3 = i1**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))