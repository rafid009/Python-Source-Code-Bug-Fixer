import numpy as np 

def function(x):

	k9 = x
	m7 = x
	paths = []
	try:
		if k9 <= 4:
			m7 = k9/7
			m7 = 4/8
			paths.append(1)
		else:
			m7 = m7*m7
			paths.append(2)
		if m7 <= 5:
			x = x/6
			k9 = k9-x
			paths.append(3)
		else:
			x = k9*3
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))