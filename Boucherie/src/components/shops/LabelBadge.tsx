interface LabelBadgeProps {
  label: string;
  isActive?: boolean;
  onClick?: () => void;
}

export const LabelBadge = ({ label, isActive, onClick }: LabelBadgeProps) => {
  return (
    <button
      onClick={onClick}
      className={`px-3 py-1 rounded-full text-xs font-medium border transition-colors ${isActive ? "bg-primary text-white border-primary" : "bg-secondary text-secondary-foreground border-transparent"}`}
    >
      {label}
    </button>
  );
};