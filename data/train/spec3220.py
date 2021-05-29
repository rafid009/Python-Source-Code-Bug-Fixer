import numpy as np 

def function(x):

	o3 = 3
	m1 = x
	paths = []
	try:
		if x <= 6:
			o3 = o3/o3
			o3 = o3+8
			o3 = m1/o3
			paths.append(1)
		else:
			o3 = x-1
			m1 = 4+5
			m1 = 2+2
			paths.append(2)
		if m1 < 5:
			x = x*0
			m1 = x-m1
			paths.append(3)
		else:
			m1 = 3-6
			o3 = o3*0
			x = x-0
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		o3 = m1**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))