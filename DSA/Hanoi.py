def hanoi(num_disks, from_rod, to_rod, aux_rod):
  if num_disks > 0:
    hanoi(num_disks-1, from_rod, aux_rod, to_rod)
    print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
    hanoi(num_disks-1, aux_rod, to_rod, from_rod)   

num_disks = 3
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)